import React, { useState } from "react";

function App() {
  const [response, setResponse] = useState("");
  const [query, setQuery] = useState(""); // New state to store the query

  const runSpider = async () => {
    try {
      const formattedQuery = query.includes(" ") ? `"${query}"` : query;
      const res = await fetch(
        `http://127.0.0.1:8000/run_spider/?query=${encodeURIComponent(
          formattedQuery
        )}`
      );
      setResponse(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleQueryChange = (event) => {
    setQuery(event.target.value);
  };

  return (
    <div>
      <h1>FYR</h1>
      <input
        type="text"
        value={query}
        onChange={handleQueryChange}
        placeholder="Enter query"
      />
      <button onClick={runSpider}>Run Spider</button>
      <p>{response}</p>
    </div>
  );
}

export default App;
