import React, { useState } from "react";
import { Card, Button } from "react-bootstrap";

function Query2() {
  const handleQuery2 = () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "content-type": "application/json",
      },
    };

    fetch("http://localhost:5000/query/query2", requestOptions)
      .then((res) => res.json())
      .then((data) => {
        document.getElementById("card").innerHTML = data.Query2;
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
          onClick={handleQuery2}
          size="sm"
        >
          Execute
        </Button>

        <Button
          variant="primary"
          style={{
            boxShadow: "rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px",
          }}
          onClick={handleReset}
          size="sm"
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
          <Card.Title>
            All subject on which Java programming language is tought:
            <br />
            <br />
            <br />
          </Card.Title>
          <Card.Text id="card"></Card.Text>
        </Card.Body>
      </Card>
    </div>
  );
}

export default Query2;
