const SliderValues = ({currentValue, min, max}) => {
    return (

        <div className="SliderValues">
            <p className="leftSliderValue">{min}</p>
            <p className="middleSliderValue">{currentValue}</p>
            <p className="rightSliderValue">{max}</p>
        </div>);
}
export default SliderValues;