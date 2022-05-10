import mmap.purdey.model.MMapMutableSubList;
import mmap.purdey.model.Quake;

import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;

/**
 * Quake collection which contains sub collections which group quakes by distance.
 */
public class QuakeSubCollection extends QuakeCollection implements Serializable
{
	private static final long serialVersionUID = 696182852669631398L;

	/**
	 * sub collection for quakes greater than the radius away
	 */
	private QuakeCollection greaterThanRadius;
	
	/**
	 * sub collection for quakes between 0 and radius away
	 */
	private QuakeCollection betweenRadius;
	
	/**
	 * sub collection for quakes without a distance to be solved
	 */
	private QuakeCollection unknownDistance;
	
	/**
	 * sub collection for quakes with no known distance (that is, 0 == unknown)
	 */
	private QuakeCollection unsetDistance;
	
	/**
	 * Constructor
