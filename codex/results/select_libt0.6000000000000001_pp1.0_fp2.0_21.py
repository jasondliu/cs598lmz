import selector from './selector';

import {
    getChartData,
    getChartConfig,
    getChartType,
    getChartId,
} from './selectors';

import {
    chartIdChanged,
    chartTypeChanged,
    chartConfigChanged,
    chartDataChanged,
    chartDataPointAdded,
    chartDataPointRemoved,
} from './actions';

const formId = 'chart-form';

const mapStateToProps = (state, ownProps) => ({
    chartId: getChartId(state),
    chartType: getChartType(state),
    chartConfig: getChartConfig(state),
    chartData: getChartData(state),
});

const mapDispatchToProps = (dispatch, ownProps) => ({
    onChartIdChanged: (value) => dispatch(chartIdChanged(value)),
    onChartTypeChanged: (value) => dispatch(chartTypeChanged(value)),
    onChartConfigChanged: (value) => dispatch(chartConfigChanged(value)),
    onChartDataChanged: (value) => dispatch(
