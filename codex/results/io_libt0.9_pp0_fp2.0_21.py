import io.aiff.format.AiffFormat;
import io.aiff.format.AiffReader;

import java.io.File;
import java.io.IOException;
import java.util.Locale;

import javax.swing.JFrame;
import javax.swing.UIManager;

import marytts.client.MaryClient;
import marytts.client.http.Address;
import marytts.exceptions.NoSuchPropertyException;
import marytts.exceptions.SynthesisException;
import marytts.modules.synthesis.Voice;
import marytts.signalproc.effects.Effect;
import marytts.signalproc.effects.PitchScaleEffect;
import marytts.signalproc.effects.RobotiserEffect;
import marytts.signalproc.effects.RobotiserEffect.Type;
import marytts.util.data.audio.AudioPlayer;

/**
 * Generate an .aiff file from the supplied text.
 * @author <
