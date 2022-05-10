import selectedClass from '../../../../../../../utils/selectClass';
import selectOffer from '../../../../../../../utils/selectOffer';
import selectOfferClass from '../../../../../../../utils/selectOfferClass';
import selectOfferClassTaken from '../../../../../../../utils/selectOfferClassTaken';

import './styles.scss';

const Classes = ({
  classes,
  offers,
  classesTaken,
}) => (
  <div className="classes">
    <div className="classes__header">
      <h2 className="classes__title">Classes</h2>
    </div>
    {
      classes.map((classItem) => {
        const offer = selectOffer(offers, classItem.offer.id);
        const offerClass = selectOfferClass(offer, classItem.id);
        const classTaken = selectOfferClassTaken(classesTaken, offerClass);
        const classTakenWithClass = classTaken ? selectedClass(classTaken) : null;
