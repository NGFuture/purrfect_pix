import React, { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import { useDispatch, useSelector } from "react-redux";

import DjangoImgSrc from "../../assets/images/django-logo-negative.png";
import { fetchRestCheck } from "../store/rest_check";

const Home = () => {
  const dispatch = useDispatch();
  const restCheck = useSelector((state) => state.restCheck);
  const [cats, setCats] = useState([]);
  useEffect(() => {
    const action = fetchRestCheck();
    dispatch(action);
  }, [dispatch]);

  useEffect(() => {
    fetch("/api/cats/list-cats/").then((response) => {  
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    }).then((data) => {
      setCats(data.items);
    })
  }, []);

  const [showBugComponent, setShowBugComponent] = useState(false);

  return (
    <>
      <h2>Static assets</h2>
      {/* <div id="django-background">
        If you are seeing the green Django logo on a white background and this
        text color is #092e20, frontend static files serving is working:
      </div> */}
      <div id="django-logo-wrapper">
        <div>
          Below this text, you should see an img tag with the white Django logo
          on a green background:
        </div>
        <img alt="Django Negative Logo" src={DjangoImgSrc} />
      </div>
      <h2>Rest API</h2>
      <p>{restCheck?.data?.payload?.result}</p>
      <Button variant="outline-dark" onClick={() => setShowBugComponent(true)}>
        Click to test if Sentry is capturing frontend errors! (Should only work
        in Production)
      </Button>
      {showBugComponent && showBugComponent.field.notexist}
      <h2>CATS</h2>
      <div className="row">
        {cats.map((cat) => (
          <div className="col-md-4" key={cat.id}>
            <div className="card">
              <img className="card-img-top" src={cat.url} alt="Cat" />
              <div className="card-body">
                <h5 className="card-title">Cat</h5>
                <p className="card-text">{cat.url}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default Home;
