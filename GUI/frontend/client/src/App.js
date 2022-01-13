import "antd/dist/antd.css"; // or 'antd/dist/antd.less'
import CustomLayout from "./containers/Layout";
import { BrowserRouter as Router } from "react-router-dom";

function App() {
  return (
    <Router>
      <CustomLayout></CustomLayout>
    </Router>
  );
}

export default App;
