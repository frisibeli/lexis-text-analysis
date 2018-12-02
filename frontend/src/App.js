import React, { Component } from 'react';
import EmotionDecectionView from './components/EmotionDetectionView/EmotionDetectionView';
import './App.css';


class App extends Component {
  render() {
    return (
      <div className="App">
        <EmotionDecectionView />
      </div>
    );
  }
}

export default App;
