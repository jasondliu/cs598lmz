import select from '../../api/select';
import { setLoader } from '../../actions/common';
import "./styles/select.css";

const Select = (props) => {
    const { label, name, options, onChange, value, error, labelStyle, inputStyle, loader } = props;

    const onChangeHandler = (event) => {
        onChange(name, event.target.value);
    };

    const renderOptions = () => {
        return options.map(option => {
            return (
                <option key={option.value} value={option.value}>{option.name}</option>
            )
        });
    };

    return (
        <div className="container__select">
            <label className={`container__select__label ${labelStyle}`}>
                {label}
            </label>
            <select className={`container__select__input ${inputStyle}`} onChange={onChangeHandler} value={value}>
                <option defaultValue style={{ display: 'none' }}></option>
                {renderOptions
