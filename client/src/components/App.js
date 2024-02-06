import { Routes, Route } from "react-router";
import Home from "./Home";

import Restaurant from "./Restaurant";

function App() {
  return (
   
      <Routes>
        <Route exact path="/restaurants/:id" element={<Restaurant />} />
          
        <Route exact path="/" element={<Home />} />
          
       
      </Routes>
  
  );
}


export default App;
