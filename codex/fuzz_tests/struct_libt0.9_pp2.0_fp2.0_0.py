import _structsVotesPost from 'src/actionCreators/structs/votesPost'

describe(`actionCreator structs/votesPost()`, () => {

  let stubbedStruct

  beforeEach(() => {
    stubbedStruct = sinon.stub(structs, `votesPost`)
  })

  it(`should be a function`, () => {
    expect(structsVotesPost).to.be.a(`function`)
  })

  it(`should call structs/votesPost() with the passed arguments`, () => {
    stubbedStruct.returns(`structed`)
    const result = structsVotesPost(`arg1`, `arg2`, `arg3`)
    expect(stubbedStruct).to.be.calledWithExactly(`arg1`, `arg2`, `arg3`)
    expect(result).to.equal(`structed`)
  })

})
