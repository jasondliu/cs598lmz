import selector from 'selectors/emailWidgets';

const EmailWidget = ({email, moved}) => {
  return (
    <div className="scroll">
      <h2>{email.get('title')}</h2>
      <p>{email.get('text')}</p>
    
