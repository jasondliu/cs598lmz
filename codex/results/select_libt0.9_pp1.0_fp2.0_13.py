import selectn from 'selectn'
import tinycolor from 'tinycolor2'
import Chart from '../Chart'

class ColumnsChart extends Component {

  adjustHeight = () => {
    const { data } = this.props
    var maxLength = 0
    data.forEach(d => {
      if (d.length > maxLength) {
        maxLength = d.length
      }
    })
    return maxLength * 80
  }
  drawComponents = (data, xKey) => {
    const { XAxis, YAxis, Columns } = Chart
    const {
      height,
      yKeys,
      padding,
      xDomain,
      backgroundColor,
      tooltip
    } = this.props
    const realHeight = height || this.adjustHeight()
    const y = YAxis()
      .height(realHeight - padding * 2)
      .padding(padding)
    const yTicks = y.ticks
    const x = XAxis()
      .width(800 - padding * 2)
      .height(realHeight - padding
