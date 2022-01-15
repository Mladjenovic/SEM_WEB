import React, { useState } from "react";
import { Card, Button } from "react-bootstrap";

function Query1() {
  const [professorName, setProfessorName] = useState("");

  const handleQuery1 = () => {
    var profName = document.getElementById("professorName").value;
    const body = {
      professor_name: profName,
    };

    const requestOptions = {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify(body),
    };

    fetch("http://localhost:5000/query/query1", requestOptions)
      .then((res) => res.json())
      .then((data) => {
        console.log(data.Query1.map((x) => x));

        document.getElementById("card").innerHTML =
          "<ul>" + data.Query1.map((x) => "<li>" + x + "</li>") + "</ul>";
      })
      .catch((err) => console.log(err));
  };

  const handleReset = () => {
    document.getElementById("card").innerHTML = "";
  };
  return (
    <div>
      <Card>
        <input id="professorName" placeholder="Enter profesor name"></input>
        <Button
          variant="primary"
          style={{
            margin: "auto",
            width: "20%",
            boxShadow: "rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px",
          }}
          onClick={handleQuery1}
          size="sm"
        >
          Execute
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
          <Card.Title>Subjects that the professor is teaching</Card.Title>
          <Card.Text id="card">
            <br />
          </Card.Text>
        </Card.Body>
      </Card>
    </div>
  );
}

export default Query1;
