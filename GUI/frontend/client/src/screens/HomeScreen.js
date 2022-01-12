import React from "react";
import { Card, Button } from "react-bootstrap";

function HomeScreen() {
  const handleQuery1 = () => {
    const requestOptions = {
      method: "GET",
    };

    fetch("http://localhost:5000/query/query1", requestOptions)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        document.getElementById("card").innerHTML = data.Query1;
      })
      .catch((err) => console.log(err));
  };

  const handleReset = () => {
    document.getElementById("card").innerHTML = "";
  };
  return (
    <div>
      <Card>
        <Button
          variant="primary"
          style={{
            margin: "auto",
            width: "20%",
            boxShadow: "rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px",
          }}
          onClick={handleQuery1}
        >
          Execute query 1
        </Button>

        <Button
          variant="primary"
          style={{
            marginLeft: "5px",
            boxShadow: "rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px",
          }}
          onClick={handleReset}
        >
          Reset
        </Button>
        <br />
        <br />
        <br />

        <Card.Body
          style={{
            boxShadow:
              "rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px",
            padding: "5px",
            width: "50%",
          }}
        >
          <Card.Title>Description for query one</Card.Title>
          <Card.Text id="card">
            <br />
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </Card.Text>
        </Card.Body>
      </Card>
    </div>
  );
}

export default HomeScreen;
