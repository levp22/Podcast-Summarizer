// import './App.css';

// import React, { useState } from 'react';

// function TextBlurbCreator({ selectedType }) {
//   const [blurbs, setBlurbs] = useState([""]);

//   const handleBlurbChange = (index, event) => {
//     const newBlurbs = [...blurbs];
//     newBlurbs[index] = event.target.value;
//     setBlurbs(newBlurbs);
//   };

//   const addBlurb = () => {
//     setBlurbs([...blurbs, ""]);
//   };

//   const removeBlurb = (index) => {
//     const newBlurbs = blurbs.filter((_, blurbIndex) => blurbIndex !== index);
//     setBlurbs(newBlurbs);
//   };

//   const handleSubmit = async (event) => {
//     event.preventDefault();
//     try {
//       const payload = {
//         type: selectedType, // Include the selected type in the payload
//         links: blurbs,
//       };
//       const response = await fetch('http://127.0.0.1:5000/posts', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(payload),
//       });
//       // Handle success here
//     } catch (error) {
//       console.error('Error:', error);
//       // Handle error here
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       {blurbs.map((blurb, index) => (
//         <div key={index}>
//           <input
//             type="text"
//             value={blurb}
//             onChange={(event) => handleBlurbChange(index, event)}
//           />
//           <button type="button" onClick={() => removeBlurb(index)}>Remove</button>
//         </div>
//       ))}
//       <button type="button" onClick={addBlurb}>Add Blurb</button>
//       <button type="submit">Submit Links</button>
//     </form>
//   );
// }



// function App() {
//   const [selectedType, setSelectedType] = useState(0);

//   const handleTypeChange = (event) => {
//     if (event.target.value =="video"){
//       setSelectedType(1);
//     }
//     else{
//       setSelectedType(0);
//     }
//   };

//   return (
//     <div className="App">
//       <header className="App-header">
//         <label>
//           Select whether you would like to send in a playlist or video link:
//           <select onChange={handleTypeChange} value={selectedType}>
//             <option value="playlist">playlist</option>
//             <option value="video">video</option>
//           </select>
//         </label>
//         <TextBlurbCreator selectedType={selectedType} />
//       </header>
//     </div>
//   );
// }

// export default App;

import React, { useState } from 'react';
import './App.css';

function ResponseBlurb({ responseBlurb }) {
  if (!responseBlurb) return null; // Don't render anything if there's no response
  return <div><p>Response: {responseBlurb}</p></div>;
}

function TextBlurbCreator({ selectedType }) {
  const [blurb, setBlurb] = useState("");
  const [responseBlurb, setResponseBlurb] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const payload = {
        type: selectedType, // 0 for playlist, 1 for video
        link: blurb,
      };
      const response = await fetch('http://127.0.0.1:5000/posts', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });
      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }
      const data = await response.json();
      setResponseBlurb(data['Return String']); // Update state with the response data
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={blurb}
          onChange={(event) => setBlurb(event.target.value)}
        />
        <button type="submit">Submit Link</button>
      </form>
      <ResponseBlurb responseBlurb={responseBlurb} />
    </div>
  );
}

function App() {
  const [selectedType, setSelectedType] = useState("playlist");

  const handleTypeChange = (event) => {
    setSelectedType(event.target.value === "video" ? "video" : "playlist");
  };

  return (
    <div className="App">
      <header className="App-header">
        <label>
          Select whether you would like to send in a playlist or video link:
          <select onChange={handleTypeChange} value={selectedType}>
            <option value="playlist">playlist</option>
            <option value="video">video</option>
          </select>
        </label>
        <TextBlurbCreator selectedType={selectedType === "video" ? 1 : 0} />
      </header>
    </div>
  );
}

export default App;
