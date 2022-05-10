import select from 'select';
import { IButtonProps } from '../button/button';
import { IHoverCardProps } from '../HoverCard';
/**
 * {@docCategory DocumentCard}
 */
export interface IDocumentCardActivityProps extends React.Props<DocumentCardActivityBase> {
    /**
     * Gets the component ref.
     */
    componentRef?: IRefObject<IDocumentCardActivityProps>;
    /**
     * Optional override class name
     */
    className?: string;
    /**
     * Number of activities to display
     */
    numberOfActivities?: number;
    /**
     * The activity personas to render
     */
    people: IPersonaProps[];
    /**
     * Render function to render the activity personas
     */
    getPersonaProps?: (persona: IPersonaProps, index: number) => IPersonaProps;
    /**
     * Optional override for activity text
     */
    activity?: string;
    /**
     * Optional override for activity icon
     */
    activityIcon?:
