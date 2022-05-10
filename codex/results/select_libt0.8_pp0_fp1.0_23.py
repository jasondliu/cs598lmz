import selectShutterBtn from '../actions/selectShutterBtn';

class CalculatePrice extends Component {

    onClickSubmit(e) {
        e.preventDefault();
        this.props.submitData({
            weight: this.props.shutter.weight,
            width: this.props.shutter.width,
            color: this.props.shutter.color,
            fit: this.props.shutter.fit
        });
    }

    onClickShutter(e) {
        // console.log(e.target.id);
        this.props.selectShutterBtn({ num: e.target.id})
    }

    render() {

        const { shutter } = this.props;

        return (
            <div className="container-fluid">
                <div className="row">
                    <div className="col-md-12">
                        <form className="form-inline">
                            <div className="form-group">
                                <label className="">Weight: </label>
                                <
