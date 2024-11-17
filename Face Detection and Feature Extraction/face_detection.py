import cv2
import dlib

# Initialize dlib's face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Start webcam feed
cap = cv2.VideoCapture(0) # this number may be 0, 1, 2, ... depending on your system config.

# Define a function to extract the eyes based on landmarks
def extract_eyes(landmarks, frame):
    ly_coords = [landmarks.part(i).y for i in range(36, 41)]
    lx_coords = [landmarks.part(i).x for i in range(36, 41)]
    lx_min = min(lx_coords)
    lx_max= max(lx_coords)
    ly_min=min(ly_coords)
    ly_max=max(ly_coords)

    ry_coords = [landmarks.part(i).y for i in range(42, 48)]
    rx_coords = [landmarks.part(i).x for i in range(42, 48)]
    rx_min = min(rx_coords)
    rx_max= max(rx_coords)
    ry_min=min(ry_coords)
    ry_max=max(ry_coords)

    # Draw rectangles around the eyes
    cv2.rectangle(frame, (lx_min, ly_min), (lx_max, ly_max), (0, 255, 255), 2)  # Left eye
    cv2.rectangle(frame, (rx_min, ry_min), (rx_max, ry_max), (0, 255, 255), 2)  # Right eye


# Define a function to extract the mouth based on landmarks
def extract_mouth(landmarks, frame):
   
    
    # Fill in your code here after defining the extraction region.

    ry_coords = [landmarks.part(i).y for i in range(48, 59)]
    rx_coords = [landmarks.part(i).x for i in range(48, 59)]
    mx_min = min(rx_coords)
    mx_max= max(rx_coords)
    my_min=min(ry_coords)
    my_max=max(ry_coords)

    # Draw rectangle around the mouth
    cv2.rectangle(frame, (mx_min, my_min), (mx_max, my_max), (0, 0, 255), 2)

def eye_aspect_ratio(eye):
    # Fill in code here
    A = abs(eye[1][1] - eye[5][1])  
    B = abs(eye[2][1] - eye[4][1])  
    C = abs(eye[0][0] - eye[3][0])  
    
    return (A + B) / (2.0 * C)

exercise = 2 # can be 1 or 2

if exercise == 1:
    while True:
        ret, frame = cap.read()  # Capture frame-by-frame from the webcam
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

        # Detect faces
        faces = detector(gray)

        for face in faces:
            # Detect facial landmarks
            landmarks = predictor(gray, face)

            # Draw bounding box around the face
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            face_extraction = frame[ y:y+h,x:x+w]

            # Draw the facial landmarks
            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)


        extract_eyes(landmarks, frame)
        extract_mouth(landmarks, frame)


        # Display the frame with detection and landmarks
        cv2.imshow('Webcam Face Detection and Landmarking', frame)

        #print(type(frame))
        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.imwrite("face_extraction.png", face_extraction)

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

EAR_THRESHOLD = 0.25
# Number of consecutive frames the eye must be below the threshold to count as a blink
CONSEC_FRAMES = 3
frame_counter = 0
blink_counter = 0

if exercise == 2:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = detector(gray)

        for face in faces:
            landmarks = predictor(gray, face)

            # Get coordinates of the left and right eyes
            left_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]
            right_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)]

            # Calculate EAR for both eyes
            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)

            # Average EAR for both eyes
            avg_ear = (left_ear + right_ear) / 2.0

            # If EAR is below the threshold, count frames
            if avg_ear < EAR_THRESHOLD:
                frame_counter += 1
            else:
                if frame_counter >= CONSEC_FRAMES:
                    blink_counter += 1
                    print(f"Blink detected! Total blinks: {blink_counter}")
                frame_counter = 0

            # Draw the eye landmarks
            for n in range(36, 48):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

            # Display the EAR on the frame
            cv2.putText(frame, f"EAR: {avg_ear:.2f}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Show the frame
        cv2.imshow('Eye Blink Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()