import selected from '../../asserts/images/podcast/selected.png';

function Podcast() {
    return (
        <React.Fragment>
            <div className={"podcast-container"}>
                <div className={"podcast-title"}>
                    <h4>Podcasts</h4>
                </div>
                <div className={"podcast-items"}>
                    <div className={"podcast-item"}>
                        <div className="podcast-poster">
                            <img src={pod2} alt={""}/>
                        </div>
                    <div className={"podcast-detail"}>
                        <h5>Popular Podcasts</h5>
                        <p>See the most popular podcasts and what people are talking about</p>
                    </div>
                    </div>
                    <div className={"podcast-item"}>
                        <div className="podcast-poster">
                            <img src={selected} alt={""}/>
                        </div>
                        <div className={"podcast-detail"}>
                            <h5
