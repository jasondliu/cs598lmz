import mmaphson.logic.BoardBuilder;

public class SkyFactory extends BoardFactory{
	
     public Board createBoard() {
 	    BoardBuilder builder = new BoardBuilder();
    	builder.setBoardSize(10);
    	builder.setBoard(board);
    	builder.setCell("1", CellType.CLOUD);
    	builder.setCell("3", CellType.CLOUD);
    	builder.setCell("4", CellType.CLOUD);
    	builder.setCell("6", CellType.CLOUD);
    	builder.setCell("8", CellType.CLOUD);
    	builder.setCell("9", CellType.CLOUD);
    	builder.setCell("10", CellType.CLOUD);
    	return builder.build();
     }

}
