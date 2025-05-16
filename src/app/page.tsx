"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [name, setName] = useState("");
  const [location, setLocation] = useState("");

  const handleSubmit = async () => {
    try {
      await axios.post("http://localhost:8000/employees/", {
        name,
        location,
      });
      setName("");
      setLocation("");
      alert("Employee added!");
    } catch (err) {
      console.error(err);
      alert("Error adding employee");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Add Employee</h1>
      <input
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{ padding: 8, marginRight: 10 }}
      />
      <input
        placeholder="Location"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
        style={{ padding: 8, marginRight: 10 }}
      />
      <button onClick={handleSubmit} style={{ padding: 8 }}>
        Submit
      </button>
    </div>
  );
}
