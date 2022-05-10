import selectedResources from './underscore/selectedResources';

export default function (metrics) {
  metrics.groupBy = groupBy;
  metrics.multiply = multiply;
  metrics.subtract = subtract;
  metrics.add = add;
  metrics.divide = divide;
  metrics.day = day;
  metrics.month = month;
  metrics.year = year;
  metrics.dates = dates;
  metrics.custom = custom;
  metrics.selectedResources = selectedResources;
  return metrics;
}
