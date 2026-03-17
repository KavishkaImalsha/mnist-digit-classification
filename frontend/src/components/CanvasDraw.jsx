import React, { useRef, useState, useEffect } from 'react';

const CanvasDraw = () => {
  const canvasRef = useRef(null);
  const [drawing, setDrawing] = useState(false);
  const [prediction, setPrediction] = useState(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.lineWidth = 20;
    ctx.lineCap = 'round';
    ctx.strokeStyle = 'black';
  }, []);

  const startDrawing = () => setDrawing(true);
  const endDrawing = () => {
    setDrawing(false);
    const ctx = canvasRef.current.getContext('2d');
    ctx.beginPath();
  };

  const draw = (e) => {
    if (!drawing) return;
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    const ctx = canvas.getContext('2d');
    ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
  };

  const clearCanvas = () => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    setPrediction(null);
  };

  const predict = async () => {
    // const canvas = canvasRef.current;
    // const image = canvas.toDataURL('image/png');

    // const response = await fetch('http://127.0.0.1:5000/predict', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify({ image }),
    // });

    // const data = await response.json();
    // setPrediction(data.prediction);
  };

  return (
    <div className="flex flex-col items-center space-y-4">
      <canvas
        ref={canvasRef}
        width={280}
        height={280}
        className="border-2 border-black"
        onMouseDown={startDrawing}
        onMouseUp={endDrawing}
        onMouseMove={draw}
      />
      <div className="space-x-4">
        <button onClick={predict} className="px-4 py-2 bg-blue-500 text-white rounded">Predict</button>
        <button onClick={clearCanvas} className="px-4 py-2 bg-gray-500 text-white rounded">Clear</button>
      </div>
      {prediction !== null && <h2 className="text-2xl font-bold">Prediction: {prediction}</h2>}
    </div>
  );
};

export default CanvasDraw;