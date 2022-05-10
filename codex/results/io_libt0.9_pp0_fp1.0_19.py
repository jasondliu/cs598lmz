import io.hydrosphere.mist.utils.TryWithResource
import mist.api.fs._
import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs.FileSystem
import org.apache.hadoop.hdfs.DistributedFileSystem
import org.apache.hadoop.security.UserGroupInformation

import scala.util.Try


trait FileSystemFactory {
  def get(): FileSystem
}

class HdfsFileSystemFactory extends FileSystemFactory {

  val logger = Logger(getClass)

  private val conf = new Configuration(false)

  def get(): FileSystem = {
    conf.addResource(this.getClass.getClassLoader.getResourceAsStream("core-site.xml"))
    logger.debug(conf.toString)
    conf.set("fs.hdfs.impl.disable.cache", "true")
    FileSystem.get(conf)
  }
}

class KryoFileSystem extends FileSystemClient {
  val logger = Logger(getClass)

  def listDir(path
