**Handwritten Digit Recognition Web App**

**Project Overview**

This project is a full-stack AI web application that allows users to draw or input handwritten digits and get real-time predictions using a trained deep neural network.
The application demonstrates the integration of machine learning models with modern web technologies and provides an interactive user experience for digit recognition.

**Features**
    -Real-time prediction of handwritten digits (0–9)
    -Interactive user input through web interface
    -Responsive and modern UI using React + TailwindCSS
    -Backend API powered by FastAPI to serve the TensorFlow model
    -High accuracy: ~94.5% on MNIST dataset
    -Easily extendable to other classification tasks

**Tech Stack**
    -Frontend: React, TailwindCSS
    -Backend: FastAPI, Uvicorn
    -Machine Learning: TensorFlow / Keras

**Installation**
    -Backend
        python -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate
        pip install -r requirements.txt
        uvicorn main:app --reload

    -Frontend
        cd frontend
        npm install
        npm run dev

**Future Improvements**
    -Upgrade model to Convolutional Neural Network (CNN) for higher accuracy (~98%+)
    -Allow real-time drawing and prediction using webcam
    -Deploy app to public hosting (Vercel, Railway, or Render)
    -Add analytics dashboard to track prediction confidence and errors