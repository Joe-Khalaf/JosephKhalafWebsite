document.addEventListener("DOMContentLoaded", () => {
    const socket = io("/chat");
    const chatMessages = document.getElementById("chat");
    const chatInput = document.getElementById("chat-input");
    const sendButton = document.getElementById("send-button");
    const leaveButton = document.getElementById("leave-button");

    // Notify the server when a user joins
    socket.emit("joined", {});

    // Handle incoming messages
    socket.on("receive_message", (data) => {
        const messageElement = document.createElement("div");
        messageElement.classList.add("chat-message");
    
        if (data.isSystem) {
            // System messages for join/leave notifications
            messageElement.classList.add(data.isOwner ? "system-message-owner" : "system-message-guest");
        } else {
            // Chat messages from users
            messageElement.classList.add(data.isOwner ? "message-owner" : "message-guest");
        }
    
        // Add the message text to the element
        messageElement.textContent = data.message;
    
        // Append the message to the chat container
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight; // Auto-scroll
    });
    
    // Send a message
    sendButton.addEventListener("click", () => {
        const message = chatInput.value.trim();
        if (message) {
            socket.emit("send_message", { message });
            chatInput.value = ""; // Clear the input field
        }
    });

    // Handle 'send' on pressing Enter
    chatInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            sendButton.click();
        }
    });

    // Handle leaving the chat
    leaveButton.addEventListener("click", () => {
        socket.emit("left");
        window.location.href = "/home";
    });
});
