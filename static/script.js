function startListening() {
    document.getElementById("sphere").innerHTML = "Listening...";
    fetch('/voice_command', {
        method: 'POST'
    }).then(response => response.text())
    .then(result => {
        document.getElementById("result-container").innerHTML = result;
        document.getElementById("sphere").innerHTML = "Tap to speak";

        if (result.toLowerCase().includes("playing")) {
            playYouTube(result);
        }

        speak(result);
    });
}


function playYouTube(command) {
    var songNameMatch = command.match(/playing\s+(.*)/i); 
    if (songNameMatch && songNameMatch[1]) {
        var songName = songNameMatch[1].trim();
        var audioPlayer = new Audio();
        audioPlayer.src = '/play_music/' + encodeURIComponent(songName);
        audioPlayer.controls = true;

        var playerContainer = document.getElementById("player-container");
        playerContainer.innerHTML = '';
        playerContainer.appendChild(audioPlayer);
    } else {
        console.error("Unable to extract song name from the command:", command);
    }
}


function playMusic(command) {
    
    var songName = command.split('playing')[1].trim();

    fetch('/play_music/' + songName, {
        method: 'GET'
    });
}

function speak(text) {
    var utterance = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(utterance);
}
