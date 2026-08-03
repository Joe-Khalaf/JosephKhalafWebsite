document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('.project__carousel');
    const cards = document.querySelectorAll('.project__carousel a');
    const dotsContainer = document.createElement('div');
    dotsContainer.classList.add('carousel-dots');

    if (!carousel || cards.length === 0) {
        console.error('Carousel or cards not found');
        return;
    }

    // Helper function to center a card
    const centerCard = (index) => {
        const card = cards[index];
        const carouselWidth = carousel.offsetWidth;
        const cardWidth = card.offsetWidth;

        // Calculate scroll position with edge handling
        const scrollPosition = Math.max(
            0,
            Math.min(
                card.offsetLeft - (carouselWidth / 2) + (cardWidth / 2),
                carousel.scrollWidth - carouselWidth // Prevent scrolling past the last card
            )
        );

        carousel.scrollTo({
            left: scrollPosition,
            behavior: 'smooth',
        });
    };

    // Create dots dynamically
    cards.forEach((_, index) => {
        const dot = document.createElement('button');
        dot.classList.add('dot');
        if (index === 0) dot.classList.add('active');
        dot.setAttribute('data-index', index);
        dotsContainer.appendChild(dot);

        // Add click functionality to navigate to the corresponding card
        dot.addEventListener('click', () => {
            centerCard(index); // Center the card when the dot is clicked
            updateDots(index);
        });
    });

    // Append dots to the document
    carousel.parentNode.appendChild(dotsContainer);

    // Update active dot on scroll
    carousel.addEventListener('scroll', () => {
        let activeIndex = 0;

        // Find the card closest to the center of the carousel
        let minDistance = Infinity;
        cards.forEach((card, index) => {
            const distance = Math.abs(
                carousel.scrollLeft + carousel.offsetWidth / 2 - (card.offsetLeft + card.offsetWidth / 2)
            );
            if (distance < minDistance) {
                minDistance = distance;
                activeIndex = index;
            }
        });

        updateDots(activeIndex);
    });

    // Update the active dot
    const updateDots = (activeIndex) => {
        document.querySelectorAll('.dot').forEach((dot, index) => {
            dot.classList.toggle('active', index === activeIndex);
        });
    };

    // Center the first card on load after a brief delay
    setTimeout(() => {
        if (cards.length > 0) {
            centerCard(0);
        }
    }, 50); // Delay to ensure layout is ready
});
