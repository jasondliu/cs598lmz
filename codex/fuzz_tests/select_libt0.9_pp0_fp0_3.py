import select from 'd3-selection/dist/d3-selection.min';

export interface IVisProperties {
    // Stroke
    strokeColor: string;
    strokeWidth: number;
    strokeDashArray: string;
    strokeOpacity: number;

    // Fill
    fillColor: string;
    fillOpacity: number;

    // Default
    defaultColor?: string;
    defaultOpacity?: number;
  }

  export class VisUtils {
    private props: IVisProperties;

    constructor(props: IVisProperties) {
      this.props = props;
    }

    public style(
      selection: d3.Selection<d3.BaseType, {}, HTMLElement, any>,
      properties: IVisProperties) {
        const svg = select('svg');
        const style = window.getComputedStyle(svg.node());

        svg.style('background', style.getPropertyValue('--background'));
        svg.style('color', style.getPropertyValue('--foreground-color'));

       
