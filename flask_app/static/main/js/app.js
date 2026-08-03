const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');
if (menu && menuLinks) {
  menu.addEventListener('click', () => {
    const isOpen = menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
    menu.setAttribute('aria-expanded', String(isOpen));
  });
}

const reveals = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  reveals.forEach((item) => observer.observe(item));
} else {
  reveals.forEach((item) => item.classList.add('is-visible'));
}

document.querySelectorAll('[data-project-carousel]').forEach((carousel, carouselIndex) => {
  const cards = Array.from(carousel.children).filter((item) => item.matches('a'));
  if (cards.length < 2) return;

  const dots = document.createElement('div');
  dots.className = 'work-carousel-dots';
  dots.setAttribute('aria-label', `Project carousel ${carouselIndex + 1}`);

  const setActive = (activeIndex) => {
    dots.querySelectorAll('button').forEach((dot, index) => {
      dot.classList.toggle('is-active', index === activeIndex);
      dot.setAttribute('aria-current', index === activeIndex ? 'true' : 'false');
    });
  };

  cards.forEach((card, index) => {
    const dot = document.createElement('button');
    dot.type = 'button';
    dot.setAttribute('aria-label', `Show project ${index + 1} of ${cards.length}`);
    dot.addEventListener('click', () => {
      carousel.scrollTo({ left: card.offsetLeft - carousel.offsetLeft, behavior: 'smooth' });
      setActive(index);
    });
    dots.appendChild(dot);
  });

  let scrollFrame;
  carousel.addEventListener('scroll', () => {
    cancelAnimationFrame(scrollFrame);
    scrollFrame = requestAnimationFrame(() => {
      const center = carousel.scrollLeft + carousel.clientWidth / 2;
      let activeIndex = 0;
      let closestDistance = Infinity;
      cards.forEach((card, index) => {
        const cardCenter = card.offsetLeft - carousel.offsetLeft + card.offsetWidth / 2;
        const distance = Math.abs(center - cardCenter);
        if (distance < closestDistance) {
          closestDistance = distance;
          activeIndex = index;
        }
      });
      setActive(activeIndex);
    });
  }, { passive: true });

  setActive(0);
  carousel.insertAdjacentElement('afterend', dots);
});
