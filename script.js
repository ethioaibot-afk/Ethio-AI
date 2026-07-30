<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ethio AI</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<div class="container">

    <header>
        <h1>Ethio AI</h1>
    </header>

    <div id="chatBox">

        <div class="bot message">
            👋 Hello! Welcome to Ethio AI.
        </div>

        <div class="bot message">
            How can I help you today?
        </div>

    </div>

    <div class="input-area">
        <input
            type="text"
            id="userInput"
            placeholder="Ask anything..."
        >
        <button onclick="sendMessage()">Send</button>
    </div>

</div>

<script src="script.js"></script>

</body>
</html>
