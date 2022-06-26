import React, { useState, useEffect } from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home"

function App() {
  const [data, setData] = useState([{}])


  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/">
          <Route index element={<Home />} />
        </Route>
      </Routes>
    </BrowserRouter>
    )
}

export default App