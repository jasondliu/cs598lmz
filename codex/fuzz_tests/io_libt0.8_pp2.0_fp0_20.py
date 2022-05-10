import io.github.biezhi.anima.Anima;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.BorderPane;
import javafx.stage.Modality;
import javafx.stage.Stage;
import org.sql2o.Sql2o;

import java.io.IOException;

public class MainApp extends Application {
    private Stage primaryStage;
    private BorderPane rootLayout;
    private Sql2o sql2o;

    @Override
    public void start(Stage primaryStage) throws Exception {
        this.primaryStage = primaryStage;
        this.primaryStage.setTitle("Agenda");

        initRootLayout();
        showPersonOverview();

        sql2o = new Sql2o("jdbc:sqlite:agenda.db", null, null);
        Anima.open(sql2o
