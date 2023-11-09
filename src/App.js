import './App.css';
import RangeForm from "./Components/RangeForm";

function App() {

    const handleRangeFormSubmit = (data) => {
        data.preventDefault();
        console.log(data.target.elements)
    };

    return (
        // According to the documentation most of the values are between 0.0 - 1.0. To make input easier I treat them as 0 - 100 (our dataset does the same)
        // Documentation does not provide range for BPM, so I took min and max value from our dataset
        <div className="App">
            <RangeForm onSubmit={handleRangeFormSubmit}/>
        </div>
    );
}

export default App;
