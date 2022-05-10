from _struct import Struct
s = Struct.__new__(Struct)\ninit: error: module struct cannot be found"
		);
	}

	//-----------------------------------------------------------------------------------------------------------------
	// run with an invalid format
	//-----------------------------------------------------------------------------------------------------------------

	@Test public void unpackBinary1() throws IOException {
		runScript(
			"def r=new Struct('xx')\n" +
			"def x=r.packInt(1)\n" +
			"def y=r.unpackBinary(x)\n" +
			"assert y==1"::run
		);
	}

	@Test public void unpackBinary2() throws IOException {
		runScript(
			"def r=new Struct('xx')\n" +
			"def x=r.packInt(1)\n" +
			"def y=r.unpackBinary(x,1)\n" +
			"assert y==[1]"::run
		);
	}

	@Test public void unpackBinary3() throws IOException {
		runScript
