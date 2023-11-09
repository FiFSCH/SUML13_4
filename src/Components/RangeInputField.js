import SliderValues from "./SliderValues";

const SliderInput = ({text, newInput, handleNewInput, min, max}) => {
    return (
        <div>
            <label style={{
                fontWeight: 600,
                fontSize: 20
            }} htmlFor="MainInputField" className="form-label">{text}</label>
            <input name={text} className="form-range" type="range" id="MainInputField" value={newInput}
                   onChange={handleNewInput} min={min} max={max} step="1"/>
            <SliderValues min={min} max={max} currentValue={newInput}/>
        </div>);
}
export default SliderInput;