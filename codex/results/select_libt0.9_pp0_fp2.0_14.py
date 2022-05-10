import selectServerHoursData from '../utils/selectServerHoursData';
import sendDataToServer from '../utils/sendDataToServer';

const encodeData = (data) => Object.keys(data)
  .map((key) => `${key}=${encodeURIComponent(data[key])}`)
  .join('&');

const handleSubmit = (data) => {
  const encodedData = encodeData(data);
  return sendDataToServer(encodedData);
};

const makeSelectValues = createSelector(
  selectHours,
  selectServerHoursData,
  (hours, serverHoursData) => ({
    startDay: hours.dateOfFirstRecord,
    endDay: DateFns.addDays(hours.dateOfFirstRecord, 6),
    startHour: serverHoursData.startHour || '',
    endHour: serverHoursData.endHour || '',
  }),
);

const ServerHoursPageComponent = ({
  open, handleClose, handleSubmit: submit, values,
}) => (
  <div>
    <Button id="
