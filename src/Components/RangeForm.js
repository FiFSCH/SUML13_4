import {useState} from "react";
import RangeInputField from "./RangeInputField";

const RangeForm = ({onSubmit}) => {
    const [BPM, setBMP] = useState(121);
    const [Energy, setEnergy] = useState(50);
    const [Danceability, setDanceability] = useState(50);
    const [Loudness, setLoudness] = useState(-30);
    const [Liveness, setLiveness] = useState(50);
    const [Acousticness, setAcousticness] = useState(50);
    const [Speechiness, setSpeechiness] = useState(50);
    return (
        // According to the documentation most of the values are between 0.0 - 1.0. To make input easier I treat them as 0 - 100 (our dataset does the same)
        // Documentation does not provide range for BPM, so I took min and max value from our dataset
        <div className="container-fluid d-flex justify-content-center min-vh-100 align-items-center">
            <form className="card p-5 bg-dark-subtle" onSubmit={onSubmit}>
                <div className="form-group">
                    <RangeInputField text="Beats Per Minute (BPM)" newInput={BPM}
                                     handleNewInput={(e) => setBMP(e.target.value)}
                                     min={37} max={206}/>
                    <RangeInputField text="Energy" newInput={Energy} handleNewInput={(e) => setEnergy(e.target.value)}
                                     min={0}
                                     max={100}/>
                    <RangeInputField text="Danceability" newInput={Danceability}
                                     handleNewInput={(e) => setDanceability(e.target.value)} min={0} max={100}/>
                    <RangeInputField text="Loudness (dB)" newInput={Loudness}
                                     handleNewInput={(e) => setLoudness(e.target.value)} min={-60} max={0}/>
                    <RangeInputField text="Liveness" newInput={Liveness}
                                     handleNewInput={(e) => setLiveness(e.target.value)}
                                     min={0} max={100}/>
                    <RangeInputField text="Acousticness" newInput={Acousticness}
                                     handleNewInput={(e) => setAcousticness(e.target.value)} min={0} max={100}/>
                    <RangeInputField text="Speechiness" newInput={Speechiness}
                                     handleNewInput={(e) => setSpeechiness(e.target.value)} min={0} max={100}/>
                    <button type="submit" className="btn btn-primary">Submit</button>
                </div>
            </form>
        </div>
    )
}
export default RangeForm;