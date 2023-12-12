# Voice-Controlled Personal Assistant (Brayn)

## 1. Introduction

The Voice-Controlled Personal Assistant project is a Flask web application designed to perform various tasks based on voice commands. The application integrates speech recognition, text-to-speech, and external APIs to enable functionalities such as playing YouTube videos, providing information from Wikipedia, and responding to queries about the current time and day.

## 2. Project Components

### 2.1 Speech Recognition

The project utilizes the `speech_recognition` library to capture and interpret voice commands. The `recognize_audio` function captures audio from the microphone and uses Google's speech recognition service to convert it into text.

### 2.2 Text-to-Speech

Text-to-speech functionality is implemented using the `pyttsx3` library. The `speak` function takes a text input and converts it into spoken words, providing audible responses to the user.

### 2.3 Flask Web Application

The project employs the Flask framework to create a web application with two routes:
- `/`: Displays the main page.
- `/voice_command`: Handles voice commands, processes them, and triggers appropriate actions.

### 2.4 Task Execution

The application supports the following voice commands:
- Play a song on YouTube.
- Obtain information from Wikipedia.
- Retrieve the current time and day.

## 3. Implementation Details

### 3.1 Voice Command Processing

Voice commands are processed in the `/voice_command` route. The application recognizes specific phrases and triggers corresponding actions. For instance:
- Commands containing "play on YouTube" initiate a YouTube video search and playback.
- Queries beginning with "tell me about," "search for," "who is," or "what is" fetch information from Wikipedia.

### 3.2 Exception Handling

The code includes robust exception handling to manage potential issues, such as audio recognition errors, timeouts, and general exceptions. Error messages are provided to the user for improved feedback.

## 4. External APIs

The project interacts with external APIs to enhance functionality:
- **YouTube API:** Used to search for and play videos on YouTube.
- **Wikipedia API:** Retrieves summarized information about a given topic from Wikipedia.

## 5. User Interface

The user interface includes an `index.html` template for the main page and a `play_youtube.html` template to display YouTube video playback.
![image](https://github.com/naman181/Brayn-Virtual-Assistant/assets/132130598/4f093707-822e-4221-b4a2-8931087dd9c7)


## 6. Future Enhancements

- **User Authentication:** Implement user authentication to personalize the assistant's responses.
- **Natural Language Processing:** Enhance the speech recognition capabilities using advanced natural language processing techniques.
- **Dynamic Responses:** Enable the assistant to dynamically adapt its responses based on user interactions.

## 7. Conclusion

The Voice-Controlled Personal Assistant project demonstrates the integration of speech recognition and external APIs to create a versatile voice-activated system. It provides a foundation for building more sophisticated personal assistants with expanded functionalities and improved user experiences.
