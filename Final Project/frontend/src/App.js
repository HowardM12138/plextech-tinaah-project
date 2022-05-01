import FrontPage from "./components/FrontPage.js";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ReviewPageTop from "./components/ReviewPageTop.js";
import FormPage from "./components/FormPage.js";
import Comments from "./components/Comments.js";
import { Cookie } from "@mui/icons-material";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<FrontPage />} />
        <Route
          path="cafe_3"
          element={
            <div>
              <ReviewPageTop cafe_type="cafe_3" />
              <Comments />
            </div>
          }
        />
        <Route
          path="crossroads"
          element={
            <div>
              <ReviewPageTop cafe_type="crossroads" />
              <Comments />
            </div>
          }
        />
        <Route
          path="foothill"
          element={
            <div>
              <ReviewPageTop cafe_type="foothill" />
              <Comments />
            </div>
          }
        />
        <Route
          path="clark_kerr_campus"
          element={
            <div>
              <ReviewPageTop cafe_type="clark_kerr_campus" />
              <Comments />
            </div>
          }
        />
        <Route path="review_form" element={<FormPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
