/** 
 * This section adds the labels on the piano whenever any key is hovered over
 */
piano.addEventListener('hover', function() {
    key-label;
});

// Select all the white and black keys
const keys = document.querySelectorAll('.white-key, .black-key');

// Function to show all key labels
const showKeyLabels = () => {
    const keyLabels = document.querySelectorAll('.key-label');
    keyLabels.forEach(label => {
        label.style.visibility = 'visible';
    });
};

// Function to hide all key labels
const hideKeyLabels = () => {
    const keyLabels = document.querySelectorAll('.key-label');
    keyLabels.forEach(label => {
        label.style.visibility = 'hidden';
    });
};

// Add event listeners for hovering over keys
keys.forEach(key => {
    // Show key labels on mouse enter (hover)
    key.addEventListener('mouseenter', showKeyLabels);
    
    // Hide key labels on mouse leave
    key.addEventListener('mouseleave', hideKeyLabels);
});

/**
 * This section adds the sound functionality to the piano
 */
// JSON object mapping keyCodes to sound URLs
const sound = {
    65: "http://carolinegabriel.com/demo/js-keyboard/sounds/040.wav", // 'A' key
    87: "http://carolinegabriel.com/demo/js-keyboard/sounds/041.wav", // 'W' key
    83: "http://carolinegabriel.com/demo/js-keyboard/sounds/042.wav", // 'S' key
    69: "http://carolinegabriel.com/demo/js-keyboard/sounds/043.wav", // 'E' key
    68: "http://carolinegabriel.com/demo/js-keyboard/sounds/044.wav", // 'D' key
    70: "http://carolinegabriel.com/demo/js-keyboard/sounds/045.wav", // 'F' key
    84: "http://carolinegabriel.com/demo/js-keyboard/sounds/046.wav", // 'T' key
    71: "http://carolinegabriel.com/demo/js-keyboard/sounds/047.wav", // 'G' key
    89: "http://carolinegabriel.com/demo/js-keyboard/sounds/048.wav", // 'Y' key
    72: "http://carolinegabriel.com/demo/js-keyboard/sounds/049.wav", // 'H' key
    85: "http://carolinegabriel.com/demo/js-keyboard/sounds/050.wav", // 'U' key
    74: "http://carolinegabriel.com/demo/js-keyboard/sounds/051.wav", // 'J' key
    75: "http://carolinegabriel.com/demo/js-keyboard/sounds/052.wav", // 'K' key
    79: "http://carolinegabriel.com/demo/js-keyboard/sounds/053.wav", // 'O' key
    76: "http://carolinegabriel.com/demo/js-keyboard/sounds/054.wav", // 'L' key
    80: "http://carolinegabriel.com/demo/js-keyboard/sounds/055.wav", // 'P' key
    186: "http://carolinegabriel.com/demo/js-keyboard/sounds/056.wav" // ';' key
};

// Mapping keyCode to their corresponding HTML element IDs
const keyMap = {
    65: 'keyA',    // A
    87: 'keyW',    // W
    83: 'keyS',    // S
    69: 'keyE',    // E
    68: 'keyD',    // D
    70: 'keyF',    // F
    84: 'keyT',    // T
    71: 'keyG',    // G
    89: 'keyY',    // Y
    72: 'keyH',    // H
    85: 'keyU',    // U
    74: 'keyJ',    // J
    75: 'keyK',    // K
    79: 'keyO',    // O
    76: 'keyL',    // L
    80: 'keyP',    // P
    186: 'keySemi' // ;
};

// Function to play the sound based on keyCode
const playSound = (keyCode) => {
    // Prevent sounds from playing after the sequence
    if (!pianoActive) return;

    if (sound[keyCode]) {
        const audio = new Audio(sound[keyCode]);
        audio.play();  // Play the corresponding sound
    } else {
        console.log("Key does not have a mapped sound.");
    }
};

// Add event listener for keydown to handle keyboard key press
document.addEventListener('keydown', (event) => {
    const keyCode = event.keyCode;
    
    // Play the sound for the pressed key
    playSound(keyCode);
    
    // Handle sequence tracking for keyboard input
    handleKeySequence(event.key.toLowerCase());

    // Optionally highlight the key visually
    highlightKey(keyCode);
});

// Add event listener for mouse click to play sound when a key is clicked
Object.keys(keyMap).forEach((keyCode) => {
    const keyElement = document.getElementById(keyMap[keyCode]);
    if (keyElement) {
        keyElement.addEventListener('click', () => {
            // Play the sound for the clicked key
            playSound(parseInt(keyCode));
            
            // Handle sequence tracking for mouse click input
            const key = String.fromCharCode(keyCode).toLowerCase();
            handleKeySequence(key);
            
            // Optionally highlight the key visually
            highlightKey(parseInt(keyCode));
        });
    }
});

/**
 * Code to handle the "we see you" hidden event for both keyboard and mouse input
 */
let pressedKeys = '';
const requiredSequence = 'weseeyou';
let pianoActive = true;  // To disable further input once awakened

// Function to handle key presses (keyboard or mouse) and track the sequence
function handleKeySequence(key) {
    if (!pianoActive) return; // Disable further actions after awakening

    // Append the key pressed to the pressedKeys string
    pressedKeys += key;
    
    // Only keep the latest sequence length
    if (pressedKeys.length > requiredSequence.length) {
        pressedKeys = pressedKeys.slice(-requiredSequence.length);
    }

    // Check if the sequence is correct
    if (pressedKeys === requiredSequence) {
        awakenTheGreatOldOne();
    }
}

// Function to awaken the great old one
function awakenTheGreatOldOne() {
    pianoActive = false; // Disable further key presses and sound

    // Fade out the piano
    const piano = document.getElementById('piano');
    piano.style.opacity = 0;
    
    const pianoTitle = document.getElementById('piano-title');
    pianoTitle.style.opacity = 0;

    // Play creepy sound
    const audio = new Audio('static/piano/images/Creepy-piano-sound-effect.mp3');
    audio.play();   

    // After the fade, hide the piano and show the image
    setTimeout(() => {
        piano.style.display = 'none';
        document.getElementById('awakening-image').style.display = 'block';
    }, 2000);  // Match this with the transition duration
}

// Listen for keydown events
document.addEventListener('keydown', handleKeyPress);
