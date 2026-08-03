document.querySelectorAll('[data-perspective-switcher]').forEach((switcher) => {
  const buttons = Array.from(switcher.querySelectorAll('[data-perspective-button]'));
  const panels = Array.from(document.querySelectorAll('[data-perspective-panel]'));
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let activePerspective = 'overview';
  let transitionTimer;

  const showPerspective = (perspective) => {
    if (perspective === activePerspective) return;

    const currentPanel = panels.find((panel) => !panel.hidden);
    const nextPanel = panels.find((panel) => panel.dataset.perspectivePanel === perspective);
    if (!nextPanel) return;

    window.clearTimeout(transitionTimer);
    buttons.forEach((button) => {
      const selected = button.dataset.perspectiveButton === perspective;
      button.setAttribute('aria-selected', String(selected));
      button.tabIndex = selected ? 0 : -1;
    });
    switcher.dataset.activePerspective = perspective;

    const finishTransition = () => {
      if (currentPanel) {
        currentPanel.hidden = true;
        currentPanel.classList.remove('is-active', 'is-leaving');
      }
      nextPanel.hidden = false;
      nextPanel.classList.add('is-active', 'is-entering');
      requestAnimationFrame(() => {
        nextPanel.querySelectorAll('.reveal').forEach((item) => item.classList.add('is-visible'));
      });
      window.setTimeout(() => nextPanel.classList.remove('is-entering'), 480);
    };

    if (reducedMotion || !currentPanel) {
      finishTransition();
    } else {
      currentPanel.classList.add('is-leaving');
      transitionTimer = window.setTimeout(finishTransition, 180);
    }

    activePerspective = perspective;
  };

  buttons.forEach((button, index) => {
    button.addEventListener('click', () => showPerspective(button.dataset.perspectiveButton));
    button.addEventListener('keydown', (event) => {
      if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      let nextIndex = index;
      if (event.key === 'ArrowLeft') nextIndex = (index - 1 + buttons.length) % buttons.length;
      if (event.key === 'ArrowRight') nextIndex = (index + 1) % buttons.length;
      if (event.key === 'Home') nextIndex = 0;
      if (event.key === 'End') nextIndex = buttons.length - 1;
      buttons[nextIndex].focus();
      showPerspective(buttons[nextIndex].dataset.perspectiveButton);
    });
  });
});
