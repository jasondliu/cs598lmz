import io.github.scalats.core.Settings
import io.github.scalats.core.ScalaTypes
import io.github.scalats.core.TypeScriptTypes._
import io.github.scalats.core.TypeScriptWriter
import io.github.scalats.core.TypescriptConverter
import scala.collection.mutable.ListBuffer

/**
 * Generates type definitions for a Scala type.
 */
trait TypeScriptDefinitionGen extends TypeScriptWriter {
  def tsType(typ: Type, settings: Settings): TypeScriptType

  def genDefinition(
    typ: Type,
    tsType: TypeScriptType,
    settings: Settings,
    alreadyGenerated: ListBuffer[Type]): Result[Unit]

  def define(typ: Type, settings: Settings): Result[Unit] = {
    val tsType = tsType(typ, settings)
    val alreadyGenerated = new ListBuffer[Type]

    genDefinition(typ, tsType, settings, alreadyGenerated)
  }

  def define(
    typ: Type,
    tsType: Type
