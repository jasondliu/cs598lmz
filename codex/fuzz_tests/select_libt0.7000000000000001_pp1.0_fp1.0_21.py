import select from '../../../img/icon/select.png';
import notSelect from '../../../img/icon/notSelect.png';

const colors = ['#1E90FF', '#FFC0CB', '#7FFF00', '#7B68EE', '#FF7F50', '#FF8C00', '#FF0000', '#FFD700'];
const styles = {
    wrap: {
        width: '100%',
    },
    header: {
        width: '100%',
        height: 40,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        borderBottom: '1px solid #e6e6e6',
        // padding: '0 10px'
    },
    hl: {
        color: '#999',
    },
    hr: {
        color: colors[0],
    },
    hrBtn: {
        display: 'flex',
        alignItems: 'center',
    },
    body: {
        display: 'flex',
