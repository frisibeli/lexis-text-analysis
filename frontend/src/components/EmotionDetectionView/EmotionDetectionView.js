import React, { Component } from 'react'
import {Radar} from 'react-chartjs';
// import PropTypes from 'prop-types'
// import styles from './style.css'

const propTypes = {}

const defaultProps = {}

class EmotionDecectionView extends Component {
    constructor(props) {
        super(props)
        this.state = {
            hasResponse:false,
            response:{
                disgust: 0,
                fear: 5,
                feeling: "",
                happiness: 10,
                neutral: 0,
                sadness: 0,
                surprise: 0
            }
        }
        this.inputTextSubmit = this.inputTextSubmit.bind(this);
        this.chartRef = React.createRef();
    }

    inputTextSubmit(event){
        if(event.key === 'Enter'){
            let inputText = event.target.value
            fetch('http://localhost:8080/api/predict', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({'input':inputText})
            })
            .then(res => res.json())
            .then(res => {
                this.setState({
                    hasResponse:true,
                    response:{
                        disgust: res.response.disgust,
                        fear: res.response.fear,
                        feeling: res.response.feeling,
                        happiness: res.response.happiness,
                        neutral: res.response.neutral,
                        sadness: res.response.sadness,
                        surprise: res.response.surprise
                    }
                })
                window.scrollTo(0, window.innerHeight.offsetTop)
            })
        }
    }

    render() {
        return (
            <div>
                <main className="main-content">
                    <div className="fullwidth-block">
                        <div className="container">
                            <h2 className="section-title">Try Lexis</h2>
                            <small className="section-subtitle">Just type something in the textarea</small>
                            <textarea onKeyPress={this.inputTextSubmit} className="figure" placeholder="Some example text here"></textarea>
                        </div>
                    </div>
                    {this.state.hasResponse &&
                    <div className="fullwidth-block">
                        <div className="container">
                            <h2 className="section-title">Emotions in the text</h2>
                            <small className="section-subtitle">We can detect multiple types of emotion</small>
                            <Radar ref={this.chartRef} redraw data={{
                                labels:['disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise'],
                                datasets:[
                                    {
                                        label:"Emotion",
                                        fillColor: "rgba(220,220,220,0.2)",
                                        strokeColor: "rgba(220,220,220,1)",
                                        pointColor: "rgba(220,220,220,1)",
                                        pointStrokeColor: "#fff",
                                        pointHighlightFill: "#fff",
                                        pointHighlightStroke: "rgba(220,220,220,1)",
                                        data: [
                                            this.state.response.disgust, 
                                            this.state.response.fear,
                                            this.state.response.happiness,
                                            this.state.response.neutral,
                                            this.state.response.sadness,
                                            this.state.response.surprise
                                        ]
                                    }
                                ]}
                            } options={{responsive: true,
                                maintainAspectRatio: true,}} />
                        </div>
                    </div> }
                </main>
            </div>
        )
    }
}

EmotionDecectionView.propTypes = propTypes

EmotionDecectionView.defaultProps = defaultProps

export default EmotionDecectionView
