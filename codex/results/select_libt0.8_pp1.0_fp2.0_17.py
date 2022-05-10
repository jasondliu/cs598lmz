import select from 'select-dom'
import { find } from 'utils-dom'
import { getCurrentUser } from '../github-helpers'
import { isPRFile, findFileMatch, getFiles } from '../dom-helpers'
import { fileExists, isChangelogFile } from '../regex-helpers'
import { parse, hasChanges, HEAD } from '../diff-helpers'
import { getCommitMessage } from '../commit-message'

const getLastCommit = async (sha: string): Promise<Commit> => {
  const commits = await api.repos.compareCommits({
    ...ctx.repo,
    base: sha,
    head: HEAD
  })

  return commits.data.commits[0]
}

export const checkChangelog = async (
  changelogFile?: File,
  changeType: ChangeType
): Promise<boolean> => {
  const files = select.all('.file')
  const changelog = changelogFile || find(files, isChangelogFile)
 
