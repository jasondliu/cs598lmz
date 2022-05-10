import io.netty.channel.socket.SocketChannel;
/*
 * Copyright (c) 2011 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */

/**
 * Utility methods for reading and writing Google API objects from and to their JSON
 * representation.
 * <p>
 * Sample usage:
 *
 * <pre>
 * <code>
 * HttpRequestFactory requestFactory = ...;
 * GenericUrl url = new GenericUrl("https://www.googleapis.com/urlshortener/v1/url");
 *
 * // Prepare the URL representing the API
