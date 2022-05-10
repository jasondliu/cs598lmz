import select from "../../assets/select.png"

class Dropdown extends Component {
  render() {
    let icon;
    if (this.props.transaction === "Out") {
      icon = select
    } else if (this.props.transaction === "In") {
      icon = income
    } else {
      icon = transfer
    }
    return (
      <div className={styles.dropdown}>
        <span className={styles.select} onClick={this.props.handleTransaction}>
          <img
            src={icon}
            alt="income"
            className={styles.selectImage}
          />
        </span>
        <div className={styles.selectMenu}>
          <div
            className={styles.selectItem}
            onClick={() => this.props.handleTransaction("In")}
          >
            <img src={income} alt="income" className={styles.selectIcons} />
            <p>Income</p>
          </div>
          <div
            className={styles.
