import React, { Component } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor() {
    super();
    this.state = {
      fname: '',
      lname: '',
      email: '',
    };
  }

  onChange = (e) => {
    /*
      Because we named the inputs to match their
      corresponding values in state, it's
      super easy to update the state
    */
    this.setState({ [e.target.name]: e.target.value });
  }

  onSubmit = (e) => {
    e.preventDefault();
    // get our form data out of state
    const { fname, lname, email } = this.state;

    axios.post('/', { fname, lname, email })
      .then((result) => {
        //access the results here....
      });
  }

  render() {
    const { fname, lname, email } = this.state;
    console.log("inside render ", this.state);
    return (
      <form onSubmit={this.onSubmit}>
        <input
          type="text"
          name="fname"
          value={fname}
          onChange={this.onChange}
        />
        <input
          type="text"
          name="lname"
          value={lname}
          onChange={this.onChange}
        />
        <input
          type="text"
          name="email"
          value={email}
          onChange={this.onChange}
        />
        <button type="submit">Submit</button>
      </form>
    );
  }
}

export default App;
