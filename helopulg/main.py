import cv
import dlib
import pyautogui

# Initialize face detector, facial landmark detector, and mouse controller
face_detector = dlib.get_frontal_face_detector()
landmark_detector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
mouse = pyautogui

# Set screen resolution
screen_width, screen_height = mouse.size()

# Initialize mouse position to center of screen
mouse_position = (screen_width // 2, screen_height // 2)
mouse.moveTo(*mouse_position)

# Initialize video capture
cap = cv.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Convert the frame to grayscale for faster processing
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_detector(gray)

    for face in faces:
        # Detect facial landmarks in the face
        landmarks = landmark_detector(gray, face)

        # Get the position of the left and right eye landmarks
        left_eye = landmarks.part(36).x, landmarks.part(36).y
        right_eye = landmarks.part(45).x, landmarks.part(45).y

        # Calculate the midpoint between the left and right eye landmarks
        eye_center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)

        # Move the mouse pointer based on the eye position
        mouse_x = int((eye_center[0] / frame.shape[1]) * screen_width)
        mouse_y = int((eye_center[1] / frame.shape[0]) * screen_height)
        mouse_position = (mouse_x, mouse_y)
        mouse.moveTo(*mouse_position)

    # Display the frame with the mouse pointer position
    cv.circle(frame, mouse_position, 5, (0, 255, 0), -1)
    cv.imshow('frame', frame)

    # Exit if the 'q' key is pressed
    if cv.waitKey(1) == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv.destroyAllWindows()
