import selectOrder from '../query/selectOrder';
import selectOvertimeAdmission from '../query/selectOvertimeAdmission';

// 상수
const { observerInfo } = constants;
const PAGE_SIZE = 10;

let collection = (db: DB) => { return db.collection('observer'); };

// 회원가입시 수무사 생성 후 observerInfo에 데이터 추가
export const insertDefault = async (
  db: DB,
  uid: string,
): Promise<void> => {
  const observers: ObserverDocument[] = [];
  for (const [key, value] of Object.entries(observerInfo)) {
    observers.push({
      uid,
      observerId: key,
      ...value,
      status: ''
    });
  }
  const insertObservers: ObserverDocument[] = await collection(db).insertMany(observers);
  const bulk =
