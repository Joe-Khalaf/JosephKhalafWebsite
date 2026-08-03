document.addEventListener('DOMContentLoaded', () => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.album-grid, .lucky-mosaic, .movie-grid, .art-grid, .garage-gallery, .life-grid, .gymnastics-clips').forEach((group) => {
    group.querySelectorAll('[data-reveal]').forEach((item, index) => item.style.setProperty('--reveal-order', index));
  });
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('[data-reveal]').forEach((element) => revealObserver.observe(element));

  const progressLinks = Array.from(document.querySelectorAll('.about-progress a'));
  const chapterObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      progressLinks.forEach((link) => link.classList.toggle('is-active', link.hash === `#${entry.target.id}`));
    });
  }, { rootMargin: '-35% 0px -55% 0px' });
  document.querySelectorAll('[data-chapter]').forEach((chapter) => chapterObserver.observe(chapter));

  const clipObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      const video = entry.target;
      if (entry.isIntersecting && !reduceMotion) {
        video.play().then(() => video.closest('.gymnastics-clip').classList.add('is-playing')).catch(() => {});
      } else {
        video.pause();
        video.closest('.gymnastics-clip').classList.remove('is-playing');
      }
    });
  }, { threshold: 0.65 });
  document.querySelectorAll('.gymnastics-clip video').forEach((video) => {
    clipObserver.observe(video);
    video.closest('.gymnastics-clip').addEventListener('click', () => {
      if (video.paused) video.play().then(() => video.closest('.gymnastics-clip').classList.add('is-playing')).catch(() => {});
      else { video.pause(); video.closest('.gymnastics-clip').classList.remove('is-playing'); }
    });
  });

  document.querySelectorAll('[data-vinyl-cycle]').forEach((display) => {
    const template = display.dataset.frameTemplate;
    const frames = Array.from({ length: 19 }, (_, index) => template.replace('__FRAME__', index));
    let frame = 0;
    let timer = null;
    let loaded = false;
    let visible = false;
    let loadingPromise = null;
    const preload = () => loadingPromise || (loadingPromise = Promise.all(frames.map((source) => new Promise((resolve) => {
      const image = new Image();
      image.onload = image.onerror = resolve;
      image.src = source;
    }))).then(() => { loaded = true; }));
    const stop = () => { window.clearInterval(timer); timer = null; };
    const start = async () => {
      if (reduceMotion || timer) return;
      if (!loaded) await preload();
      if (!visible || document.hidden || timer) return;
      timer = window.setInterval(() => {
        frame = (frame + 1) % frames.length;
        display.src = frames[frame];
      }, 250);
    };
    const cycleObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        visible = entry.isIntersecting;
        visible ? start() : stop();
      });
    }, { rootMargin: '250px 0px', threshold: 0.05 });
    cycleObserver.observe(display);
    document.addEventListener('visibilitychange', () => document.hidden ? stop() : (visible && start()));
  });


  if (!reduceMotion) {
    const media = Array.from(document.querySelectorAll('.about-media'));
    let ticking = false;
    const updateMotion = () => {
      const viewportMiddle = window.innerHeight / 2;
      media.forEach((item, index) => {
        const box = item.getBoundingClientRect();
        if (box.bottom < 0 || box.top > window.innerHeight) return;
        const distance = (box.top + box.height / 2 - viewportMiddle) / window.innerHeight;
        const direction = index % 2 ? -1 : 1;
        item.style.setProperty('--media-y', `${Math.max(-9, Math.min(9, distance * direction * 12))}px`);
      });
      ticking = false;
    };
    window.addEventListener('scroll', () => {
      if (!ticking) requestAnimationFrame(updateMotion);
      ticking = true;
    }, { passive: true });
    updateMotion();
  }

  const lightbox = document.querySelector('.about-lightbox');
  const lightboxImage = lightbox.querySelector('img');
  const closeButton = lightbox.querySelector('button');
  document.querySelectorAll('.about-media img').forEach((image) => {
    image.tabIndex = 0;
    image.setAttribute('role', 'button');
    image.setAttribute('aria-label', `${image.alt || 'Image'} — open larger`);
    const openImage = () => {
      lightboxImage.src = image.currentSrc || image.src;
      lightboxImage.alt = image.alt;
      lightbox.showModal();
    };
    image.addEventListener('click', openImage);
    image.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        openImage();
      }
    });
  });
  closeButton.addEventListener('click', () => lightbox.close());
  lightbox.addEventListener('click', (event) => {
    if (event.target === lightbox) lightbox.close();
  });
});
