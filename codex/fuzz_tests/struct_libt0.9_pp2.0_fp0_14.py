import _struct from '../__mock__/struct.json';
import _servers from '../__mock__/servers.json';

import {
  getCorsOptions,
  getStruct,
  getServerTemplates,
  getServerTemplateKey,
} from '../../src/helpers/swaggerHelpers';

describe('swaggerHelpers', () => {
  describe('#getServerTemplates', () => {
    test('should return a template for each server', () => {
      const mockCorsOptions = getCorsOptions(_corsOptions);
      const servers = getServerTemplates(_servers, mockCorsOptions);
      expect(servers).toBeDefined();
      expect(servers[0].url).toEqual('http://localhost:{port}/{version}');
      expect(servers[1].url).toEqual('https://{domain}/{version}');
    });
    test('should return a default defined if no server present', () => {
      const mockCorsOptions = getCorsOptions(_corsOptions);
      const
